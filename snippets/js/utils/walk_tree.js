function walk(obj) {
    if (Array.isArray(obj)) {
        return obj.map(val => walk(val));
    } else if (obj instanceof Object) {
        const result = {};
        Object.entries(obj).forEach(([key, val]) => {
            result[key] = walk(val);
        });
        return result;
    } else {
       return obj;
    };
}
