## zh-CN

通过设置 `type` 自定义渲染结果，提供 `canvas` 和 `svg` 两个选项。

## en-US

Customize the rendering results by `type`, provide options `canvas` and `svg`.
```tsx
import React from 'react';
import { QRCode, Space } from 'antd';

const App: React.FC = () => (
  <Space>
    <QRCode type="canvas" value="https://ant.design/" />
    <QRCode type="svg" value="https://ant.design/" />
  </Space>
);

export default App;
```
