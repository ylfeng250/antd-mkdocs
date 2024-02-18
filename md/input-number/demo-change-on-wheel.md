## zh-CN

启用鼠标滚轮控制。

## en-US

Control with mouse wheel.
```tsx
import React from 'react';
import { InputNumber } from 'antd';

const onChange = (value: number) => {
  console.log('changed', value);
};

const App: React.FC = () => (
  <InputNumber min={1} max={10} defaultValue={3} onChange={onChange} changeOnWheel />
);

export default App;
```
