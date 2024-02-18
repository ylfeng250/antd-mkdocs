## zh-CN

用 `target` 设置 `Affix` 需要监听其滚动事件的元素，默认为 `window`。

## en-US

Set a `target` for 'Affix', which is listen to scroll event of target element (default is `window`).

<style>
#components-affix-demo-target .scrollable-container {
  height: 100px;
  overflow-y: scroll;
}
#components-affix-demo-target .background {
  padding-top: 60px;
  height: 300px;
  background-image: url('https://zos.alipayobjects.com/rmsportal/RmjwQiJorKyobvI.jpg');
}
</style>
```tsx
import React from 'react';
import { Affix, Button } from 'antd';

const containerStyle: React.CSSProperties = {
  width: '100%',
  height: 100,
  overflow: 'auto',
  border: '1px solid #40a9ff',
};

const style: React.CSSProperties = {
  width: '100%',
  height: 1000,
};

const App: React.FC = () => {
  const [container, setContainer] = React.useState<HTMLDivElement | null>(null);
  return (
    <div style={containerStyle} ref={setContainer}>
      <div style={style}>
        <Affix target={() => container}>
          <Button type="primary">Fixed at the top of container</Button>
        </Affix>
      </div>
    </div>
  );
};

export default App;
```
