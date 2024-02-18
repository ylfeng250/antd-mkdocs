## zh-CN

使用自定义指示符。

## en-US

Use custom loading indicator.
```tsx
import React from 'react';
import { LoadingOutlined } from '@ant-design/icons';
import { Spin } from 'antd';

const App: React.FC = () => <Spin indicator={<LoadingOutlined style={{ fontSize: 24 }} spin />} />;

export default App;
```
