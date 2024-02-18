## zh-CN

使用 `status` 为 TimePicker 添加状态，可选 `error` 或者 `warning`。

## en-US

Add status to TimePicker with `status`, which could be `error` or `warning`.
```tsx
import React from 'react';
import { Space, TimePicker } from 'antd';

const App: React.FC = () => (
  <Space direction="vertical">
    <TimePicker status="error" />
    <TimePicker status="warning" />
    <TimePicker.RangePicker status="error" />
    <TimePicker.RangePicker status="warning" />
  </Space>
);

export default App;
```
