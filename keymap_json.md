### Hyper
```
keymaps: {
    'editor:copy': 'ctrl+shift+c',
    'editor:paste': 'ctrl+shift+v',
},
```

### Sublime Text
```
[
    { "keys": ["ctrl+a"], "command": "select_all" },
    { "keys": ["ctrl+z"], "command": "undo" },
    { "keys": ["ctrl+x"], "command": "cut" },
    { "keys": ["ctrl+c"], "command": "copy" },
    { "keys": ["ctrl+v"], "command": "paste" },
    { "keys": ["ctrl+s"], "command": "save", "args": { "async": true } },
    { "keys": ["ctrl+n"], "command": "new_file" },
    { "keys": ["ctrl+k", "ctrl+b"], "command": "toggle_side_bar" },
    { "keys": ["ctrl+w"], "command": "close_transient", "context":
		[
			{ "key": "group_has_transient_sheet", "operator": "equal", "operand": true }
		]
	},
	{ "keys": ["ctrl+f"], "command": "show_panel", "args": {"panel": "find", "reverse": false} },
	{ "keys": ["alt+up"], "command": "swap_line_up" },
	{ "keys": ["alt+down"], "command": "swap_line_down" },
]
```
