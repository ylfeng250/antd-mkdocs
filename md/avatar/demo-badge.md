## zh-CN

通常用于消息提示。

## en-US

Usually used for reminders and notifications.
```tsx
import { UserOutlined } from '@ant-design/icons';
import React from 'react';
import { Avatar, Badge, Space } from 'antd';

const App: React.FC = () => (
  <Space size={24}>
    <Badge count={1}>
      <Avatar shape="square" icon={<UserOutlined />} />
    </Badge>
    <Badge dot>
      <Avatar shape="square" icon={<UserOutlined />} />
    </Badge>
  </Space>
);

export default App;
```
