## zh-CN

没有具体的数字。

## en-US

This will simply display a red badge, without a specific count. If count equals 0, it won't display the dot.
```tsx
import React from 'react';
import { NotificationOutlined } from '@ant-design/icons';
import { Badge, Space } from 'antd';

const App: React.FC = () => (
  <Space>
    <Badge dot>
      <NotificationOutlined style={{ fontSize: 16 }} />
    </Badge>
    <Badge dot>
      <a href="#">Link something</a>
    </Badge>
  </Space>
);

export default App;
```
