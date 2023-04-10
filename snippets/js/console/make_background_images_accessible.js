$('*').filter((_, e) =>
  $(e).css('background-image')
).each((_, e) => {
  try {
    let src = $(e).css('background-image').slice(5, -2)
    e.outerHTML = e.outerHTML.replace(/\<\w+/g, '<img')
    t0.attr('src', src)
  } catch { }
})
