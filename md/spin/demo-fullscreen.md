## zh-CN

`fullscreen` 属性非常适合创建流畅的页面加载器。它添加了半透明覆盖层，并在其中心放置了一个旋转加载符号。

## en-US

The `fullscreen` mode is perfect for creating page loaders. It adds a dimmed overlay with a centered spinner.
```tsx
import React from 'react';
import { Button, Spin } from 'antd';

const App: React.FC = () => {
  const [spinning, setSpinning] = React.useState<boolean>(false);

  const showLoader = () => {
    setSpinning(true);
    setTimeout(() => {
      setSpinning(false);
    }, 3000);
  };

  return (
    <>
      <Button onClick={showLoader}>Show fullscreen for 3s</Button>
      <Spin spinning={spinning} fullscreen />
    </>
  );
};

export default App;
```
