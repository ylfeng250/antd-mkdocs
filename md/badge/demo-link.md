## zh-CN

用 a 标签进行包裹即可。

## en-US

The badge can be wrapped with `a` tag to make it linkable.
```tsx
import React from 'react';
import { Avatar, Badge } from 'antd';

const App: React.FC = () => (
  <a href="#">
    <Badge count={5}>
      <Avatar shape="square" size="large" />
    </Badge>
  </a>
);

export default App;
```
