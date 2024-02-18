## zh-CN

通过 `destroyTooltipOnHide` 控制提示关闭时是否销毁 dom 节点。

## en-US

Setting `destroyTooltipOnHide` to control whether destroy dom node of tooltip when hidden.
```tsx
import React from 'react';
import { Tooltip } from 'antd';

const App: React.FC = () => (
  <Tooltip destroyTooltipOnHide title="prompt text">
    <span>Tooltip will destroy when hidden.</span>
  </Tooltip>
);

export default App;
```
