## zh-CN

Select 默认针对大数据开启了[虚拟滚动](https://github.com/react-component/virtual-list)，因而获得了更好的性能，可以通过 `virtual={false}` 关闭。

## en-US

Select use [virtual scroll](https://github.com/react-component/virtual-list) which get better performance, turn off it by set `virtual={false}`.
```tsx
import React from 'react';
import type { SelectProps } from 'antd';
import { Select, Typography } from 'antd';

const { Title } = Typography;

const options: SelectProps['options'] = [];

for (let i = 0; i < 100000; i++) {
  const value = `${i.toString(36)}${i}`;
  options.push({
    label: value,
    value,
    disabled: i === 10,
  });
}

const handleChange = (value: string[]) => {
  console.log(`selected ${value}`);
};

const App: React.FC = () => (
  <>
    <Title level={4}>{options.length} Items</Title>
    <Select
      mode="multiple"
      style={{ width: '100%' }}
      placeholder="Please select"
      defaultValue={['a10', 'c12']}
      onChange={handleChange}
      options={options}
    />
  </>
);

export default App;
```
