jq '[recurse(.children[]) | del(.children)]'
