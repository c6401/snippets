Vue.component('MyButton', {
  template: `
    <span>
      <button @click="click">click</button>
    </span>
  `,
  methods: {
    click() {
      alert('click');
    },
  },
});
