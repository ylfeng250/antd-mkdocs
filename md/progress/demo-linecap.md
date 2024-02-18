## zh-CN

通过设定 `strokeLinecap="butt"` 可以调整进度条边缘的形状为方形，详见 [stroke-linecap](https://developer.mozilla.org/docs/Web/SVG/Attribute/stroke-linecap)。

## en-US

By setting `strokeLinecap="butt"`, you can change the linecaps from `round` to `butt`, see [stroke-linecap](https://developer.mozilla.org/docs/Web/SVG/Attribute/stroke-linecap) for more information.
```tsx
import React from 'react';
import { Progress, Space } from 'antd';

const App: React.FC = () => (
  <>
    <Progress strokeLinecap="butt" percent={75} />
    <Space wrap>
      <Progress strokeLinecap="butt" type="circle" percent={75} />
      <Progress strokeLinecap="butt" type="dashboard" percent={75} />
    </Space>
  </>
);

export default App;
```
