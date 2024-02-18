## zh-CN

标签形式的多选框，用户亦可自由输入。

## en-US

Allow user to select tags from list or input custom tag.
```tsx
import React from 'react';
import { Select } from 'antd';
import type { SelectProps } from 'antd';

const options: SelectProps['options'] = [];

for (let i = 10; i < 36; i++) {
  options.push({
    value: i.toString(36) + i,
    label: i.toString(36) + i,
  });
}

const handleChange = (value: string) => {
  console.log(`selected ${value}`);
};

const App: React.FC = () => (
  <Select
    mode="tags"
    style={{ width: '100%' }}
    placeholder="Tags Mode"
    onChange={handleChange}
    options={options}
  />
);

export default App;
```