vim.keymap.set({ "n", "i" }, "<S-CR>", function()
  local line = vim.api.nvim_get_current_line()
  local term = require("snacks.terminal")
  local t = term.get() or term.open({ win = { position = "bottom" } })
  local chan = vim.bo[t.buf].channel
  vim.api.nvim_chan_send(chan, line .. "\n")
  vim.cmd("normal! j")
end, { desc = "Send line to terminal" })
