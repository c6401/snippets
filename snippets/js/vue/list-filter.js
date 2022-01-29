// <list-filter :items="[{ name: 'cherry' }, { name: 'strawberry' }, { name: 'orange' }, { name: 'apple' }]"><list-filter>
Vue.component('list-filter', {
  template: `
    <span>
      <input type="text" v-model="filter">
      <div v-for="item in filtered" :key="item.id">
        <div>{{ item.name }}</div>
      </div>
    </span>
  `,
  props: { items: Array },
  computed: {
    filtered() {
      return this.items.filter(item => {
        return item.name.toLowerCase().includes(this.filter.toLowerCase())
      })
    }
  },
  data() {
    return { filter: '' };
  },
});
