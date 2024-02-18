## zh-CN

使用 `status` 为 DatePicker 添加状态，可选 `error` 或者 `warning`。

## en-US

Add status to DatePicker with `status`, which could be `error` or `warning`.
```tsx
import React from 'react';
import { DatePicker, Space } from 'antd';

const App: React.FC = () => (
  <Space direction="vertical" style={{ width: '100%' }}>
    <DatePicker status="error" style={{ width: '100%' }} />
    <DatePicker status="warning" style={{ width: '100%' }} />
    <DatePicker.RangePicker status="error" style={{ width: '100%' }} />
    <DatePicker.RangePicker status="warning" style={{ width: '100%' }} />
  </Space>
);

export default App;
```