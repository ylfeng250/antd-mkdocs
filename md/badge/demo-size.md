## zh-CN

可以设置有数字徽标的大小。

## en-US

Set size of numeral Badge.
```tsx
import React from 'react';
import { Avatar, Badge, Space } from 'antd';

const App: React.FC = () => (
  <Space size="middle">
    <Badge size="default" count={5}>
      <Avatar shape="square" size="large" />
    </Badge>
    <Badge size="small" count={5}>
      <Avatar shape="square" size="large" />
    </Badge>
  </Space>
);

export default App;
```
