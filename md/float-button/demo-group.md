## zh-CN

按钮组合使用时，推荐使用 `<FloatButton.Group />`，并通过设置 `shape` 属性改变悬浮按钮组的形状。悬浮按钮组的 `shape` 会覆盖内部 FloatButton 的 `shape` 属性。

## en-US

When multiple buttons are used together, `<FloatButton.Group />` is recommended. By setting `shape` of FloatButton.Group, you can change the shape of group. `shape` of FloatButton.Group will override `shape` of FloatButton inside.
```tsx
import React from 'react';
import { QuestionCircleOutlined, SyncOutlined } from '@ant-design/icons';
import { FloatButton } from 'antd';

const App: React.FC = () => (
  <>
    <FloatButton.Group shape="circle" style={{ right: 24 }}>
      <FloatButton icon={<QuestionCircleOutlined />} />
      <FloatButton />
      <FloatButton.BackTop visibilityHeight={0} />
    </FloatButton.Group>
    <FloatButton.Group shape="square" style={{ right: 94 }}>
      <FloatButton icon={<QuestionCircleOutlined />} />
      <FloatButton />
      <FloatButton icon={<SyncOutlined />} />
      <FloatButton.BackTop visibilityHeight={0} />
    </FloatButton.Group>
  </>
);

export default App;
```
