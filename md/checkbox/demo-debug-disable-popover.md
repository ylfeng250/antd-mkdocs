## zh-CN

禁用时鼠标进入、离开触发 Tooltip

## en-US

Disable to show/hide Tooltip
```tsx
import React from 'react';
import { Checkbox, Popover } from 'antd';

const App: React.FC = () => (
  <div style={{ padding: 56 }}>
    <Popover content="xxxx" trigger="hover">
      <Checkbox disabled checked />
    </Popover>
  </div>
);

export default App;
```
