## zh-CN

基本标签的用法，可以通过设置 `closeIcon` 变为可关闭标签并自定义关闭按钮，设置为 `true` 时将使用默认关闭按钮。可关闭标签具有 `onClose` 事件。

## en-US

Usage of basic Tag, and it could be closable and customize close button by set `closeIcon` property, will display default close button when `closeIcon` is setting to `true`. Closable Tag supports `onClose` events.
```tsx
import { CloseCircleOutlined } from '@ant-design/icons';
import React from 'react';
import { Space, Tag } from 'antd';

const log = (e: React.MouseEvent<HTMLElement>) => {
  console.log(e);
};

const preventDefault = (e: React.MouseEvent<HTMLElement>) => {
  e.preventDefault();
  console.log('Clicked! But prevent default.');
};

const App: React.FC = () => (
  <Space size={[0, 8]} wrap>
    <Tag>Tag 1</Tag>
    <Tag>
      <a href="https://github.com/ant-design/ant-design/issues/1862">Link</a>
    </Tag>
    <Tag closeIcon onClose={preventDefault}>
      Prevent Default
    </Tag>
    <Tag closeIcon={<CloseCircleOutlined />} onClose={log}>
      Tag 2
    </Tag>
  </Space>
);

export default App;
```
