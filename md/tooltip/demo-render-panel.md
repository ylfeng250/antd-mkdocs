## zh-CN

调试用组件，请勿直接使用。

## en-US

Debug usage. Do not use in your production.
```tsx
import React from 'react';
import { Tooltip } from 'antd';

const { _InternalPanelDoNotUseOrYouWillBeFired: InternalTooltip } = Tooltip;

const App: React.FC = () => (
  <>
    <InternalTooltip title="Hello, Pink Pure Panel!" color="pink" />
    <InternalTooltip title="Hello, Customize Color Pure Panel!" color="#f50" />
    <InternalTooltip title="Hello, Pure Panel!" placement="bottomLeft" style={{ width: 200 }} />
  </>
);

export default App;
```
