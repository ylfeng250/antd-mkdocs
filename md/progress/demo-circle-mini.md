## zh-CN

小一号的圈形进度。

## en-US

A smaller circular progress bar.
```tsx
import React from 'react';
import { Progress, Space } from 'antd';

const App: React.FC = () => (
  <Space wrap>
    <Progress type="circle" percent={30} size={80} />
    <Progress type="circle" percent={70} size={80} status="exception" />
    <Progress type="circle" percent={100} size={80} />
  </Space>
);

export default App;
```
