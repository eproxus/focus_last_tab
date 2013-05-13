Focus Last Tab for Sublime Text
===============================

Always focus the last tab with Ctrl+9 or ⌘+9 in Sublime Text 2 or 3, just
like in your favorite browser!

Installation
------------

Clone this repository into your `Packages` folder (Sublime Text 3 on OS X):

```sh
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages
git clone git://github.com/eproxus/focus_last_tab.git "Focus Last Tab"
```

Customize
---------

To customize, add your desired key binding to
_Preferences -> Key Bindings - User_:

```json
[
    { "keys": ["ctrl+end"], "command": "last_view" }
]
```

To keep the default key binding, add the following to
_Preferences -> Settings - User_:

```json
{
    "focus_last_tab_override": false
}
```
