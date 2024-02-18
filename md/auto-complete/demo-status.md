## zh-CN

使用 `status` 为 AutoComplete 添加状态，可选 `error` 或者 `warning`。

## en-US

Add status to AutoComplete with `status`, which could be `error` or `warning`.
```tsx
import React, { useState } from 'react';
import { AutoComplete, Space } from 'antd';

const mockVal = (str: string, repeat = 1) => ({
  value: str.repeat(repeat),
});

const App: React.FC = () => {
  const [options, setOptions] = useState<{ value: string }[]>([]);
  const [anotherOptions, setAnotherOptions] = useState<{ value: string }[]>([]);

  const getPanelValue = (searchText: string) =>
    !searchText ? [] : [mockVal(searchText), mockVal(searchText, 2), mockVal(searchText, 3)];

  return (
    <Space direction="vertical" style={{ width: '100%' }}>
      <AutoComplete
        options={options}
        onSearch={(text) => setOptions(getPanelValue(text))}
        status="error"
        style={{ width: 200 }}
      />
      <AutoComplete
        options={anotherOptions}
        onSearch={(text) => setAnotherOptions(getPanelValue(text))}
        status="warning"
        style={{ width: 200 }}
      />
    </Space>
  );
};

export default App;
```
