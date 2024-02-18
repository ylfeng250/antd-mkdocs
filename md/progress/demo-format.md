## zh-CN

`format` 属性指定格式。

## en-US

You can set a custom text by setting the `format` prop.
```tsx
import React from 'react';
import { Progress, Space } from 'antd';

const App: React.FC = () => (
  <Space wrap>
    <Progress type="circle" percent={75} format={(percent) => `${percent} Days`} />
    <Progress type="circle" percent={100} format={() => 'Done'} />
  </Space>
);

export default App;
```
