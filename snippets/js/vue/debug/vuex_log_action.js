plugins: [
  store => store.subscribeAction(
      action => console.log('🔴', action.type, [action.payload])
  ),
]
