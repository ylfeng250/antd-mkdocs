## zh-CN

可选 `outlined` `filled` `borderless` 三种形态。

## en-US

There are `outlined` `fille` and `borderless`, totally three variants to choose from.
```tsx
import React, { useState } from 'react';
import { AutoComplete, Flex } from 'antd';

const mockVal = (str: string, repeat = 1) => ({
  value: str.repeat(repeat),
});

const App: React.FC = () => {
  const [options, setOptions] = useState<{ value: string }[]>([]);

  const getPanelValue = (searchText: string) =>
    !searchText ? [] : [mockVal(searchText), mockVal(searchText, 2), mockVal(searchText, 3)];

  return (
    <Flex vertical gap={12}>
      <AutoComplete
        options={options}
        style={{ width: 200 }}
        placeholder="Outlined"
        onSearch={(text) => setOptions(getPanelValue(text))}
        onSelect={globalThis.console.log}
      />
      <AutoComplete
        options={options}
        style={{ width: 200 }}
        placeholder="Filled"
        onSearch={(text) => setOptions(getPanelValue(text))}
        onSelect={globalThis.console.log}
        variant="filled"
      />
      <AutoComplete
        options={options}
        style={{ width: 200 }}
        placeholder="Borderless"
        onSearch={(text) => setOptions(getPanelValue(text))}
        onSelect={globalThis.console.log}
        variant="borderless"
      />
    </Flex>
  );
};

export default App;
```