## zh-CN

`size="small"` 表示小号开关。

## en-US

`size="small"` represents a small sized switch.
```tsx
import React from 'react';
import { Switch } from 'antd';

const App: React.FC = () => (
  <>
    <Switch defaultChecked />
    <br />
    <Switch size="small" defaultChecked />
  </>
);

export default App;
```
