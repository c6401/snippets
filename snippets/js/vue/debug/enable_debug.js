app = Array.from(document.querySelectorAll('*')).find((e) => e.__vue_app__).__vue_app__
devtools = window.__VUE_DEVTOOLS_GLOBAL_HOOK__
devtools.enabled = true
devtools.emit('app:init', app, app.version, {})
