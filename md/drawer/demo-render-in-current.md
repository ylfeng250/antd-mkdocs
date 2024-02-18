## zh-CN

渲染在当前 dom 里。自定义容器，查看 `getContainer`。

> 注意：在 v5 中 `style` 与 `className` 迁移至 Drawer 面板上与 Modal 保持一致，原 `style` 与 `className` 替换为 `rootStyle` 与 `rootClassName`。

> 当 `getContainer` 返回 DOM 节点时，需要手动设置 `rootStyle` 为 `{ position: 'absolute' }`，参考 [#41951](https://github.com/ant-design/ant-design/issues/41951#issuecomment-1521099152)。

## en-US

Render in current dom. custom container, check `getContainer`.

> Note: `style` and `className` props are moved to Drawer panel in v5 which is aligned with Modal component. Original `style` and `className` props are replaced by `rootStyle` and `rootClassName`.

> When `getContainer` returns a DOM node, you need to manually set `rootStyle` to `{ position: 'absolute' }`, see [#41951](https://github.com/ant-design/ant-design/issues/41951#issuecomment-1521099152).
```tsx
import React, { useState } from 'react';
import { Button, Drawer, theme } from 'antd';

const App: React.FC = () => {
  const { token } = theme.useToken();
  const [open, setOpen] = useState(false);

  const showDrawer = () => {
    setOpen(true);
  };

  const onClose = () => {
    setOpen(false);
  };

  const containerStyle: React.CSSProperties = {
    position: 'relative',
    height: 200,
    padding: 48,
    overflow: 'hidden',
    background: token.colorFillAlter,
    border: `1px solid ${token.colorBorderSecondary}`,
    borderRadius: token.borderRadiusLG,
  };

  return (
    <div style={containerStyle}>
      Render in this
      <div style={{ marginTop: 16 }}>
        <Button type="primary" onClick={showDrawer}>
          Open
        </Button>
      </div>
      <Drawer
        title="Basic Drawer"
        placement="right"
        closable={false}
        onClose={onClose}
        open={open}
        getContainer={false}
      >
        <p>Some contents...</p>
      </Drawer>
    </div>
  );
};

export default App;
```
