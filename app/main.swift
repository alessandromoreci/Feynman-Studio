// Feynman Studio — native macOS shell around index.html (WKWebView).
// Built by build_app.sh; no Xcode project needed.

import Cocoa
import WebKit

final class AppDelegate: NSObject, NSApplicationDelegate, NSWindowDelegate,
                         WKNavigationDelegate, WKUIDelegate, WKDownloadDelegate, WKScriptMessageHandler, NSMenuDelegate {

    var window: NSWindow!
    var webView: WKWebView!

    // MARK: - Launch

    func applicationDidFinishLaunching(_ notification: Notification) {
        buildMainMenu()

        let config = WKWebViewConfiguration()
        // the page lives on file://; let it read its own files and use blob/canvas exports freely
        config.preferences.setValue(true, forKey: "allowFileAccessFromFileURLs")
        config.setValue(true, forKey: "allowUniversalAccessFromFileURLs")
        config.preferences.javaScriptCanOpenWindowsAutomatically = false
        // bridge to the page: window colour, haptics, PDF clipboard (see "Bridge" below)
        config.userContentController.add(self, name: "fs")
        config.userContentController.addUserScript(WKUserScript(
            source: "window.__fsMacApp = true; document.documentElement.classList.add('mac-app');",
            injectionTime: .atDocumentStart, forMainFrameOnly: true))

        webView = WKWebView(frame: NSRect(x: 0, y: 0, width: 1440, height: 900), configuration: config)
        webView.navigationDelegate = self
        webView.uiDelegate = self
        webView.allowsMagnification = true
        webView.allowsBackForwardNavigationGestures = false
        if #available(macOS 13.3, *) { webView.isInspectable = false }   // the page holds API keys in memory: no Web Inspector from outside

        window = NSWindow(contentRect: NSRect(x: 0, y: 0, width: 1440, height: 900),
                          styleMask: [.titled, .closable, .miniaturizable, .resizable],
                          backing: .buffered, defer: false)
        window.title = "Feynman Studio"
        // one surface: no grey title bar, its colour follows the top of the app (sent by the page)
        window.titlebarAppearsTransparent = true
        window.titleVisibility = .hidden
        if #available(macOS 11.0, *) { window.titlebarSeparatorStyle = .none }
        window.minSize = NSSize(width: 900, height: 600)
        window.isReleasedWhenClosed = false
        window.collectionBehavior = [.fullScreenPrimary]
        window.backgroundColor = NSColor(srgbRed: 0.973, green: 0.976, blue: 0.984, alpha: 1) // the top of the app, until the page says otherwise
        window.delegate = self
        window.contentView = webView
        window.center()
        window.setFrameAutosaveName("FeynmanStudioMainWindow")

        loadApp()

        window.makeKeyAndOrderFront(nil)
        NSApp.activate(ignoringOtherApps: true)
    }

    func loadApp() {
        guard let webDir = Bundle.main.resourceURL?.appendingPathComponent("web", isDirectory: true) else { return }
        let index = webDir.appendingPathComponent("index.html")
        webView.loadFileURL(index, allowingReadAccessTo: webDir)
    }

    func applicationShouldHandleReopen(_ sender: NSApplication, hasVisibleWindows flag: Bool) -> Bool {
        if !flag { window.makeKeyAndOrderFront(nil) }
        return true
    }

    func applicationShouldTerminateAfterLastWindowClosed(_ sender: NSApplication) -> Bool { false }

    // MARK: - Menu

    func buildMainMenu() {
        let main = NSMenu()
        func item(_ menu: NSMenu, _ title: String, _ action: Selector, _ key: String = "", _ mods: NSEvent.ModifierFlags = [.command], cmd: String? = nil) {
            let it = menu.addItem(withTitle: title, action: action, keyEquivalent: key)
            it.keyEquivalentModifierMask = mods
            if let c = cmd { it.representedObject = c; it.target = self }
        }
        let js = #selector(runCommand(_:))

        // App menu
        let appItem = NSMenuItem(); main.addItem(appItem)
        let appMenu = NSMenu()
        appMenu.addItem(withTitle: "About Feynman Studio", action: #selector(NSApplication.orderFrontStandardAboutPanel(_:)), keyEquivalent: "")
        appMenu.addItem(.separator())
        item(appMenu, "Settings…", js, ",", cmd: "appearance")
        appMenu.addItem(.separator())
        appMenu.addItem(withTitle: "Hide Feynman Studio", action: #selector(NSApplication.hide(_:)), keyEquivalent: "h")
        let hideOthers = appMenu.addItem(withTitle: "Hide Others", action: #selector(NSApplication.hideOtherApplications(_:)), keyEquivalent: "h")
        hideOthers.keyEquivalentModifierMask = [.command, .option]
        appMenu.addItem(withTitle: "Show All", action: #selector(NSApplication.unhideAllApplications(_:)), keyEquivalent: "")
        appMenu.addItem(.separator())
        appMenu.addItem(withTitle: "Quit Feynman Studio", action: #selector(NSApplication.terminate(_:)), keyEquivalent: "q")
        appItem.submenu = appMenu

        // File
        let fileItem = NSMenuItem(); main.addItem(fileItem)
        let fileMenu = NSMenu(title: "File")
        item(fileMenu, "New Diagram", js, "t", cmd: "newTab")
        let openIt = fileMenu.addItem(withTitle: "Open…", action: #selector(openProject(_:)), keyEquivalent: "o")
        openIt.target = self
        let recentItem = fileMenu.addItem(withTitle: "Open Recent", action: nil, keyEquivalent: "")
        recentMenu.delegate = self
        recentItem.submenu = recentMenu
        fileMenu.addItem(.separator())
        item(fileMenu, "Save Project", js, "s", cmd: "save")
        item(fileMenu, "Export…", js, "e", cmd: "export")
        item(fileMenu, "Copy as PDF", js, "c", [.command, .shift], cmd: "copyPDF")
        item(fileMenu, "Share…", js, cmd: "share")
        fileMenu.addItem(.separator())
        let printIt = fileMenu.addItem(withTitle: "Print…", action: #selector(printDiagram(_:)), keyEquivalent: "p")
        printIt.target = self
        fileMenu.addItem(.separator())
        fileMenu.addItem(withTitle: "Close Window", action: #selector(NSWindow.performClose(_:)), keyEquivalent: "w")
        fileItem.submenu = fileMenu

        // Edit (the standard items keep Cmd+C / Cmd+V / Cmd+A working inside text fields)
        let editItem = NSMenuItem(); main.addItem(editItem)
        let editMenu = NSMenu(title: "Edit")
        editMenu.addItem(withTitle: "Undo", action: Selector(("undo:")), keyEquivalent: "z")
        let redo = editMenu.addItem(withTitle: "Redo", action: Selector(("redo:")), keyEquivalent: "z")
        redo.keyEquivalentModifierMask = [.command, .shift]
        editMenu.addItem(.separator())
        editMenu.addItem(withTitle: "Cut", action: #selector(NSText.cut(_:)), keyEquivalent: "x")
        editMenu.addItem(withTitle: "Copy", action: #selector(NSText.copy(_:)), keyEquivalent: "c")
        editMenu.addItem(withTitle: "Paste", action: #selector(NSText.paste(_:)), keyEquivalent: "v")
        item(editMenu, "Duplicate", js, "d", cmd: "duplicate")
        editMenu.addItem(withTitle: "Select All", action: #selector(NSText.selectAll(_:)), keyEquivalent: "a")
        editItem.submenu = editMenu

        // View
        let viewItem = NSMenuItem(); main.addItem(viewItem)
        let viewMenu = NSMenu(title: "View")
        item(viewMenu, "All Diagrams", js, cmd: "overview")
        item(viewMenu, "Focus Mode", js, cmd: "focus")
        item(viewMenu, "Command Palette", js, "k", cmd: "palette")
        viewMenu.addItem(.separator())
        item(viewMenu, "Zoom In", js, cmd: "zoomIn")
        item(viewMenu, "Zoom Out", js, cmd: "zoomOut")
        item(viewMenu, "Fit Diagram", js, cmd: "zoomFit")
        viewMenu.addItem(.separator())
        let themeItem = viewMenu.addItem(withTitle: "Appearance", action: nil, keyEquivalent: "")
        let themeMenu = NSMenu(title: "Appearance")
        for (title, mode) in [("Light", "light"), ("Dark", "dark"), ("Automatic", "auto")] {
            let it = themeMenu.addItem(withTitle: title, action: #selector(setTheme(_:)), keyEquivalent: "")
            it.target = self; it.representedObject = mode
            themeItems.append(it)
        }
        themeItem.submenu = themeMenu
        viewMenu.addItem(.separator())
        viewMenu.addItem(withTitle: "Reload", action: #selector(reloadPage(_:)), keyEquivalent: "")   // no shortcut: a reload empties the canvas and forgets the AI keys, it must not happen by accident
        let fs = viewMenu.addItem(withTitle: "Enter Full Screen", action: #selector(NSWindow.toggleFullScreen(_:)), keyEquivalent: "f")
        fs.keyEquivalentModifierMask = [.command, .control]
        viewItem.submenu = viewMenu

        // Window
        let winItem = NSMenuItem(); main.addItem(winItem)
        let winMenu = NSMenu(title: "Window")
        winMenu.addItem(withTitle: "Minimize", action: #selector(NSWindow.performMiniaturize(_:)), keyEquivalent: "m")
        winMenu.addItem(withTitle: "Zoom", action: #selector(NSWindow.performZoom(_:)), keyEquivalent: "")
        winMenu.addItem(.separator())
        winMenu.addItem(withTitle: "Feynman Studio", action: #selector(showMainWindow(_:)), keyEquivalent: "1")
        winItem.submenu = winMenu
        NSApp.windowsMenu = winMenu

        // Help
        let helpItem = NSMenuItem(); main.addItem(helpItem)
        let helpMenu = NSMenu(title: "Help")
        item(helpMenu, "Getting Started", js, cmd: "help")
        item(helpMenu, "Keyboard Shortcuts", js, "/", cmd: "shortcuts")
        item(helpMenu, "What's New", js, cmd: "whatsNew")
        helpItem.submenu = helpMenu
        NSApp.helpMenu = helpMenu

        NSApp.mainMenu = main
    }

    var themeItems: [NSMenuItem] = []
    let recentMenu = NSMenu(title: "Open Recent")
    var pageReady = false
    var pendingOpen: [URL] = []

    // MARK: - Projects: Finder (double-click, drop on the Dock icon), Open…, Open Recent

    func application(_ application: NSApplication, open urls: [URL]) {
        for url in urls { openURL(url) }
    }

    func openURL(_ url: URL) {
        guard pageReady else { pendingOpen.append(url); return }   // launched by a double-click: wait for the page
        guard let text = try? String(contentsOf: url, encoding: .utf8),
              let data = try? JSONSerialization.data(withJSONObject: [text, url.lastPathComponent]),
              let args = String(data: data, encoding: .utf8) else { return }
        js("(function(a){ window.__fsCmd && window.__fsCmd('openText', a[0], a[1]); })(\(args))")
        noteRecent(url)
        window.makeKeyAndOrderFront(nil)
    }

    var recents: [String] {
        get { UserDefaults.standard.stringArray(forKey: "recentProjects") ?? [] }
        set { UserDefaults.standard.set(Array(newValue.prefix(10)), forKey: "recentProjects") }
    }

    func noteRecent(_ url: URL) {
        recents = [url.path] + recents.filter { $0 != url.path }
    }

    func menuNeedsUpdate(_ menu: NSMenu) {
        guard menu === recentMenu else { return }
        menu.removeAllItems()
        let list = recents.filter { FileManager.default.fileExists(atPath: $0) }
        for path in list {
            let it = menu.addItem(withTitle: (path as NSString).lastPathComponent, action: #selector(openRecent(_:)), keyEquivalent: "")
            it.target = self; it.representedObject = path; it.toolTip = path
        }
        if !list.isEmpty { menu.addItem(.separator()) }
        let clear = menu.addItem(withTitle: "Clear Menu", action: list.isEmpty ? nil : #selector(clearRecents(_:)), keyEquivalent: "")
        clear.target = self
    }

    @objc func openRecent(_ sender: NSMenuItem) {
        if let p = sender.representedObject as? String { openURL(URL(fileURLWithPath: p)) }
    }

    @objc func clearRecents(_ sender: Any?) { recents = [] }

    // MARK: - Print (only the diagram, prepared by the page)

    @objc func printDiagram(_ sender: Any?) {
        webView.evaluateJavaScript("window.__fsCmd ? window.__fsCmd('preparePrint') : false") { [weak self] result, _ in
            guard let self = self, (result as? Bool) == true else { return }
            let info = NSPrintInfo.shared.copy() as! NSPrintInfo
            info.horizontalPagination = .fit
            info.verticalPagination = .fit
            info.isHorizontallyCentered = true
            info.isVerticallyCentered = false
            let op = self.webView.printOperation(with: info)
            op.view?.frame = self.webView.bounds
            op.runModal(for: self.window, delegate: self, didRun: #selector(self.printDone(_:success:contextInfo:)), contextInfo: nil)
        }
    }

    @objc func printDone(_ op: NSPrintOperation, success: Bool, contextInfo: UnsafeMutableRawPointer?) {
        js("window.__fsCmd && window.__fsCmd('endPrint')")
    }

    // MARK: - Share (macOS share menu: AirDrop, Mail, Messages, Notes…)

    func share(pdf: Data, name: String) {
        let url = FileManager.default.temporaryDirectory.appendingPathComponent(name + ".pdf")
        guard (try? pdf.write(to: url, options: .atomic)) != nil else { return }
        let picker = NSSharingServicePicker(items: [url])
        let b = webView.bounds
        let y: CGFloat = webView.isFlipped ? 64 : b.maxY - 64
        picker.show(relativeTo: NSRect(x: b.maxX - 120, y: y, width: 1, height: 1), of: webView, preferredEdge: .minY)
    }

    // MARK: - Bridge with the page

    func js(_ code: String) { webView.evaluateJavaScript(code, completionHandler: nil) }

    @objc func runCommand(_ sender: NSMenuItem) {
        guard let c = sender.representedObject as? String else { return }
        js("window.__fsCmd && window.__fsCmd('\(c)')")
    }

    @objc func setTheme(_ sender: NSMenuItem) {
        guard let m = sender.representedObject as? String else { return }
        js("window.__fsCmd && window.__fsCmd('theme', '\(m)')")
        themeItems.forEach { $0.state = ($0.representedObject as? String) == m ? .on : .off }
    }

    @objc func openProject(_ sender: Any?) {
        let panel = NSOpenPanel()
        panel.canChooseFiles = true
        panel.canChooseDirectories = false
        panel.allowsMultipleSelection = false
        panel.allowedFileTypes = ["json"]
        panel.beginSheetModal(for: window) { [weak self] result in
            guard let self = self, result == .OK, let url = panel.url,
                  let text = try? String(contentsOf: url, encoding: .utf8),
                  let data = try? JSONSerialization.data(withJSONObject: [text, url.lastPathComponent]),
                  let args = String(data: data, encoding: .utf8) else { return }
            self.js("(function(a){ window.__fsCmd && window.__fsCmd('openText', a[0], a[1]); })(\(args))")
            self.noteRecent(url)
        }
    }

    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
        guard message.name == "fs", let body = message.body as? [String: Any], let type = body["type"] as? String else { return }
        switch type {
        case "haptic":
            // the small click of the trackpad when a guide catches (as in Keynote)
            NSHapticFeedbackManager.defaultPerformer.perform(.alignment, performanceTime: .now)
        case "chrome":
            if let css = body["color"] as? String, let c = AppDelegate.color(css) { window.backgroundColor = c }
            let dark = (body["dark"] as? Bool) ?? false
            window.appearance = NSAppearance(named: dark ? .darkAqua : .aqua)
        case "copy":
            let pb = NSPasteboard.general
            pb.clearContents()
            if let b = body["pdf"] as? String, let d = Data(base64Encoded: b) { pb.setData(d, forType: .pdf) }
            if let b = body["png"] as? String, let d = Data(base64Encoded: b) { pb.setData(d, forType: .png) }
        case "ready":
            let mode = (body["theme"] as? String) ?? "light"
            themeItems.forEach { $0.state = ($0.representedObject as? String) == mode ? .on : .off }
            pageReady = true
            let waiting = pendingOpen; pendingOpen = []
            waiting.forEach { openURL($0) }
        case "open":
            openProject(nil)
        case "print":
            printDiagram(nil)
        case "doc":
            // the diagram's name (Window menu, Mission Control) and the dot of unsaved changes in the red button
            window.title = (body["title"] as? String) ?? "Feynman Studio"
            window.isDocumentEdited = (body["edited"] as? Bool) ?? false
        case "share":
            if let b = body["pdf"] as? String, let d = Data(base64Encoded: b) {
                share(pdf: d, name: (body["name"] as? String) ?? "Feynman diagram")
            }
        default: break
        }
    }

    // "rgb(r, g, b)" or "rgba(r, g, b, a)" → NSColor
    static func color(_ css: String) -> NSColor? {
        let nums = css.components(separatedBy: CharacterSet(charactersIn: "0123456789.").inverted)
                      .filter { !$0.isEmpty }.compactMap { Double($0) }
        guard nums.count >= 3 else { return nil }
        return NSColor(srgbRed: CGFloat(nums[0] / 255), green: CGFloat(nums[1] / 255), blue: CGFloat(nums[2] / 255), alpha: 1)
    }

    @objc func reloadPage(_ sender: Any?) { pageReady = false; webView.reload() }
    @objc func zoomReset(_ sender: Any?) { webView.pageZoom = 1.0 }
    @objc func zoomIn(_ sender: Any?) { webView.pageZoom = min(webView.pageZoom + 0.1, 3.0) }
    @objc func zoomOut(_ sender: Any?) { webView.pageZoom = max(webView.pageZoom - 0.1, 0.5) }
    @objc func showMainWindow(_ sender: Any?) { window.makeKeyAndOrderFront(nil) }

    // MARK: - Navigation: downloads (exports) and external links

    func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction,
                 decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {
        if navigationAction.shouldPerformDownload {
            decisionHandler(.download)
            return
        }
        if let url = navigationAction.request.url, let scheme = url.scheme?.lowercased(),
           ["http", "https", "mailto"].contains(scheme),
           navigationAction.targetFrame?.isMainFrame ?? true {
            // links to GitHub, docs, papers… open in the default browser, not inside the app
            NSWorkspace.shared.open(url)
            decisionHandler(.cancel)
            return
        }
        decisionHandler(.allow)
    }

    func webView(_ webView: WKWebView, decidePolicyFor navigationResponse: WKNavigationResponse,
                 decisionHandler: @escaping (WKNavigationResponsePolicy) -> Void) {
        decisionHandler(navigationResponse.canShowMIMEType ? .allow : .download)
    }

    func webView(_ webView: WKWebView, navigationAction: WKNavigationAction, didBecome download: WKDownload) {
        download.delegate = self
    }

    func webView(_ webView: WKWebView, navigationResponse: WKNavigationResponse, didBecome download: WKDownload) {
        download.delegate = self
    }

    func download(_ download: WKDownload, decideDestinationUsing response: URLResponse,
                  suggestedFilename: String, completionHandler: @escaping (URL?) -> Void) {
        let panel = NSSavePanel()
        panel.nameFieldStringValue = suggestedFilename
        panel.canCreateDirectories = true
        panel.isExtensionHidden = false
        panel.beginSheetModal(for: window) { result in
            guard result == .OK, let url = panel.url else { completionHandler(nil); return }
            if FileManager.default.fileExists(atPath: url.path) {
                try? FileManager.default.removeItem(at: url)   // the panel already asked "Replace?"
            }
            completionHandler(url)
        }
    }

    func download(_ download: WKDownload, didFailWithError error: Error, resumeData: Data?) {
        let alert = NSAlert(error: error)
        alert.beginSheetModal(for: window, completionHandler: nil)
    }

    // the web content process can die (e.g. after sleep); bring the page back
    func webViewWebContentProcessDidTerminate(_ webView: WKWebView) { webView.reload() }

    // MARK: - UI: <input type=file>, alert, confirm, prompt

    func webView(_ webView: WKWebView, runOpenPanelWith parameters: WKOpenPanelParameters,
                 initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping ([URL]?) -> Void) {
        let panel = NSOpenPanel()
        panel.canChooseFiles = true
        panel.canChooseDirectories = parameters.allowsDirectories
        panel.allowsMultipleSelection = parameters.allowsMultipleSelection
        panel.beginSheetModal(for: window) { result in
            completionHandler(result == .OK ? panel.urls : nil)
        }
    }

    func webView(_ webView: WKWebView, runJavaScriptAlertPanelWithMessage message: String,
                 initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping () -> Void) {
        let alert = NSAlert()
        alert.messageText = "Feynman Studio"
        alert.informativeText = message
        alert.addButton(withTitle: "OK")
        alert.beginSheetModal(for: window) { _ in completionHandler() }
    }

    func webView(_ webView: WKWebView, runJavaScriptConfirmPanelWithMessage message: String,
                 initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping (Bool) -> Void) {
        let alert = NSAlert()
        alert.messageText = "Feynman Studio"
        alert.informativeText = message
        alert.addButton(withTitle: "OK")
        alert.addButton(withTitle: "Cancel")
        alert.beginSheetModal(for: window) { r in completionHandler(r == .alertFirstButtonReturn) }
    }

    func webView(_ webView: WKWebView, runJavaScriptTextInputPanelWithPrompt prompt: String,
                 defaultText: String?, initiatedByFrame frame: WKFrameInfo,
                 completionHandler: @escaping (String?) -> Void) {
        let alert = NSAlert()
        alert.messageText = "Feynman Studio"
        alert.informativeText = prompt
        let field = NSTextField(frame: NSRect(x: 0, y: 0, width: 280, height: 24))
        field.stringValue = defaultText ?? ""
        alert.accessoryView = field
        alert.addButton(withTitle: "OK")
        alert.addButton(withTitle: "Cancel")
        alert.beginSheetModal(for: window) { r in
            completionHandler(r == .alertFirstButtonReturn ? field.stringValue : nil)
        }
    }
}

let app = NSApplication.shared
let delegate = AppDelegate()
app.delegate = delegate
app.setActivationPolicy(.regular)
app.run()
