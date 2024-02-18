## zh-CN

静态方法无法消费 Context，推荐优先使用 Hooks 版本。

## en-US

Static methods cannot consume Context. Please use hooks first.
```tsx
import React from 'react';
import { Button, message } from 'antd';

const info = () => {
  message.info('This is a normal message');
};

const App: React.FC = () => (
  <Button type="primary" onClick={info}>
    Static Method
  </Button>
);

export default App;
```
