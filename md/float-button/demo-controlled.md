## zh-CN

通过 `open` 设置组件为受控模式，需要配合 trigger 一起使用。

## en-US

Set the component to controlled mode through `open`, which need to be used together with trigger.
```tsx
import { CommentOutlined, CustomerServiceOutlined } from '@ant-design/icons';
import React, { useState } from 'react';
import { FloatButton, Switch } from 'antd';

const App: React.FC = () => {
  const [open, setOpen] = useState(true);

  const onChange = (checked: boolean) => {
    setOpen(checked);
  };

  return (
    <>
      <FloatButton.Group
        open={open}
        trigger="click"
        style={{ right: 24 }}
        icon={<CustomerServiceOutlined />}
      >
        <FloatButton />
        <FloatButton icon={<CommentOutlined />} />
      </FloatButton.Group>
      <Switch onChange={onChange} checked={open} style={{ margin: 16 }} />
    </>
  );
};

export default App;
```
