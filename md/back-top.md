
## custom demo
>/demo/custom.tsx


可以自定义回到顶部按钮的样式，限制宽高：`40px * 40px`。

> 注意：`BackTop` 需要一个可接受 `onClick` 事件的元素作为 `children`。 如果您直接将文本作为子项放置，则该组件将无法正常运行。



You can customize the style of the button, just note the size limit: no more than `40px * 40px`.

> Note: `BackTop` expects a element could accept `onClick` property as children. If you put a text directly as children the component will not function properly.
```tsx
import React from 'react';
import { BackTop } from 'antd';

const style: React.CSSProperties = {
  height: 40,
  width: 40,
  lineHeight: '40px',
  borderRadius: 4,
  backgroundColor: '#1088e9',
  color: '#fff',
  textAlign: 'center',
  fontSize: 14,
};

const App: React.FC = () => (
  <div style={{ height: '600vh', padding: 8 }}>
    <div>Scroll to bottom</div>
    <div>Scroll to bottom</div>
    <div>Scroll to bottom</div>
    <div>Scroll to bottom</div>
    <div>Scroll to bottom</div>
    <div>Scroll to bottom</div>
    <div>Scroll to bottom</div>
    <BackTop>
      <div style={style}>UP</div>
    </BackTop>
  </div>
);

export default App;
```

## basic demo
>/demo/basic.tsx


最简单的用法。



The most basic usage.

```css
.site-back-top-basic {
  color: rgba(64, 64, 64, 0.6);
}
```
```tsx
import React from 'react';
import { BackTop } from 'antd';

const App: React.FC = () => (
  <>
    <BackTop />
    Scroll down to see the bottom-right
    <strong className="site-back-top-basic"> gray </strong>
    button.
  </>
);

export default App;
```
