const yaml = obj =>
  obj == null ? 'null' :
  Array.isArray(obj) ? obj.map((v,i) => `- ${yaml(v)}`).join('\n') :
  typeof obj === 'object' ?
    Object.entries(obj).map(([k,v]) =>
      `${k}: ${typeof v === 'object' && v !== null ?
        '\n' + yaml(v).replace(/^/gm, '  ') : v}`
    ).join('\n') :
  obj;
