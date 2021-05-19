from IPython.display import HTML, Javascript

Javascript(f'window.names={names};')

%%javascript
require.config({paths: {vue: "https://cdnjs.cloudflare.com/ajax/libs/vue/2.4.0/vue"}});

require(["vue"], function(Vue) {
  window.app = new Vue({
    el: '#app',
    data: {
      names: names,
    },
  })
})

%%html
<div id="app">
  <div v-for="name in ['test']">
    {{ name }}
  </div>
</div>
