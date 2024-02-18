## zh-CN

通过 `shape` 设置不同的形状。

## en-US

Change the shape of the FloatButton with `shape`.
```tsx
import React from 'react';
import { CustomerServiceOutlined } from '@ant-design/icons';
import { FloatButton } from 'antd';

const App: React.FC = () => (
  <>
    <FloatButton
      shape="circle"
      type="primary"
      style={{ right: 94 }}
      icon={<CustomerServiceOutlined />}
    />
    <FloatButton
      shape="square"
      type="primary"
      style={{ right: 24 }}
      icon={<CustomerServiceOutlined />}
    />
  </>
);

export default App;
```
