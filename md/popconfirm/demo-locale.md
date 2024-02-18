## zh-CN

使用 `okText` 和 `cancelText` 自定义按钮文字。

## en-US

Set `okText` and `cancelText` props to customize the button's labels.
```tsx
import React from 'react';
import { Button, Popconfirm } from 'antd';

const App: React.FC = () => (
  <Popconfirm
    title="Delete the task"
    description="Are you sure to delete this task?"
    okText="Yes"
    cancelText="No"
  >
    <Button danger>Delete</Button>
  </Popconfirm>
);

export default App;
```
