## zh-CN

checkbox 不可用。

## en-US

Disabled checkbox.
```tsx
import React from 'react';
import { Checkbox } from 'antd';

const App: React.FC = () => (
  <>
    <Checkbox defaultChecked={false} disabled />
    <br />
    <Checkbox indeterminate disabled />
    <br />
    <Checkbox defaultChecked disabled />
  </>
);

export default App;
```
