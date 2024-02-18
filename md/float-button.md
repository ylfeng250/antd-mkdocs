## interface

```tsx
import type React from 'react';

import type { BadgeProps } from '../badge';
import type { TooltipProps } from '../tooltip';
import type BackTop from './BackTop';
import type Group from './FloatButtonGroup';
import type PurePanel from './PurePanel';

export type FloatButtonElement = HTMLAnchorElement & HTMLButtonElement;

export interface FloatButtonRef {
  nativeElement: FloatButtonElement | null;
}

export type FloatButtonType = 'default' | 'primary';

export type FloatButtonShape = 'circle' | 'square';

export type FloatButtonGroupTrigger = 'click' | 'hover';

export type FloatButtonBadgeProps = Omit<BadgeProps, 'status' | 'text' | 'title' | 'children'>;

export interface FloatButtonProps extends React.DOMAttributes<FloatButtonElement> {
  prefixCls?: string;
  className?: string;
  rootClassName?: string;
  style?: React.CSSProperties;
  icon?: React.ReactNode;
  description?: React.ReactNode;
  type?: FloatButtonType;
  shape?: FloatButtonShape;
  tooltip?: TooltipProps['title'];
  href?: string;
  target?: React.HTMLAttributeAnchorTarget;
  badge?: FloatButtonBadgeProps;
  ['aria-label']?: React.HtmlHTMLAttributes<HTMLElement>['aria-label'];
}

export interface FloatButtonContentProps extends React.DOMAttributes<HTMLDivElement> {
  className?: string;
  icon?: FloatButtonProps['icon'];
  description?: FloatButtonProps['description'];
  prefixCls: FloatButtonProps['prefixCls'];
}

export interface FloatButtonGroupProps extends FloatButtonProps {
  // 包含的 Float Button
  children: React.ReactNode;
  // 触发方式 (有触发方式为菜单模式）
  trigger?: FloatButtonGroupTrigger;
  // 受控展开
  open?: boolean;
  // 关闭按钮自定义图标
  closeIcon?: React.ReactNode;
  // 展开收起的回调
  onOpenChange?: (open: boolean) => void;
}

export interface BackTopProps extends Omit<FloatButtonProps, 'target'> {
  visibilityHeight?: number;
  onClick?: React.MouseEventHandler<FloatButtonElement>;
  target?: () => HTMLElement | Window | Document;
  prefixCls?: string;
  children?: React.ReactNode;
  className?: string;
  rootClassName?: string;
  style?: React.CSSProperties;
  duration?: number;
}

export type CompoundedComponent = React.ForwardRefExoticComponent<
  FloatButtonProps & React.RefAttributes<FloatButtonElement>
> & {
  Group: typeof Group;
  BackTop: typeof BackTop;
  _InternalPanelDoNotUseOrYouWillBeFired: typeof PurePanel;
};
```

## group demo
>/demo/group.tsx


按钮组合使用时，推荐使用 `<FloatButton.Group />`，并通过设置 `shape` 属性改变悬浮按钮组的形状。悬浮按钮组的 `shape` 会覆盖内部 FloatButton 的 `shape` 属性。



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

## type demo
>/demo/type.tsx


通过 `type` 改变悬浮按钮的类型。



Change the type of the FloatButton with `type`.
```tsx
import React from 'react';
import { QuestionCircleOutlined } from '@ant-design/icons';
import { FloatButton } from 'antd';

const App: React.FC = () => (
  <>
    <FloatButton icon={<QuestionCircleOutlined />} type="primary" style={{ right: 24 }} />
    <FloatButton icon={<QuestionCircleOutlined />} type="default" style={{ right: 94 }} />
  </>
);

export default App;
```

## controlled demo
>/demo/controlled.tsx


通过 `open` 设置组件为受控模式，需要配合 trigger 一起使用。



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

## shape demo
>/demo/shape.tsx


通过 `shape` 设置不同的形状。



Change the shape of the FloatButton with `shape`.
```tsx
import React from 'react';
import { CustomerServiceOutlined } from '@ant-design/icons';
import { FloatButton } from 'antd';

const App: React.FC = () => (
  <>
    <FloatButton
      shape="circle"
      type="primary"
      style={{ right: 94 }}
      icon={<CustomerServiceOutlined />}
    />
    <FloatButton
      shape="square"
      type="primary"
      style={{ right: 24 }}
      icon={<CustomerServiceOutlined />}
    />
  </>
);

export default App;
```

## tooltip demo
>/demo/tooltip.tsx


设置 tooltip 属性，即可开启气泡卡片。



Setting `tooltip` prop to show FloatButton with tooltip.
```tsx
import React from 'react';
import { FloatButton } from 'antd';

const App: React.FC = () => <FloatButton tooltip={<div>Documents</div>} />;

export default App;
```

## description demo
>/demo/description.tsx


可以通过 `description` 设置文字内容。

> 仅当 `shape` 属性为 `square` 时支持。由于空间较小，推荐使用比较精简的双数文字。



Setting `description` prop to show FloatButton with description.

> supported only when `shape` is `square`. Due to narrow space for text, short sentence is recommended.
```tsx
import React from 'react';
import { FileTextOutlined } from '@ant-design/icons';
import { FloatButton } from 'antd';

const App: React.FC = () => (
  <>
    <FloatButton
      icon={<FileTextOutlined />}
      description="HELP INFO"
      shape="square"
      style={{ right: 24 }}
    />
    <FloatButton description="HELP INFO" shape="square" style={{ right: 94 }} />
    <FloatButton
      icon={<FileTextOutlined />}
      description="HELP"
      shape="square"
      style={{ right: 164 }}
    />
  </>
);

export default App;
```

## render-panel demo
>/demo/render-panel.tsx


调试用组件，请勿直接使用。



Debug usage. Do not use in your production.
```tsx
import { CustomerServiceOutlined, QuestionCircleOutlined, SyncOutlined } from '@ant-design/icons';
import React from 'react';
import { FloatButton } from 'antd';

/** Test usage. Do not use in your production. */
const { _InternalPanelDoNotUseOrYouWillBeFired: InternalFloatButton } = FloatButton;

const App: React.FC = () => (
  <div style={{ display: 'flex', columnGap: 16, alignItems: 'center' }}>
    <InternalFloatButton backTop />
    <InternalFloatButton icon={<CustomerServiceOutlined />} />
    <InternalFloatButton
      icon={<QuestionCircleOutlined />}
      description="HELP"
      shape="square"
      type="primary"
    />
    <InternalFloatButton
      shape="square"
      items={[
        { icon: <QuestionCircleOutlined /> },
        { icon: <CustomerServiceOutlined /> },
        { icon: <SyncOutlined /> },
      ]}
    />
    <InternalFloatButton
      open
      icon={<CustomerServiceOutlined />}
      trigger="click"
      items={[
        { icon: <QuestionCircleOutlined /> },
        { icon: <CustomerServiceOutlined /> },
        { icon: <SyncOutlined /> },
      ]}
    />
  </div>
);

export default App;
```

## group-menu demo
>/demo/group-menu.tsx


设置 `trigger` 属性即可开启菜单模式。提供 `hover` 和 `click` 两种触发方式。



Open menu mode with `trigger`, which could be `hover` or `click`.
```tsx
import { CommentOutlined, CustomerServiceOutlined } from '@ant-design/icons';
import React from 'react';
import { FloatButton } from 'antd';

const App: React.FC = () => (
  <>
    <FloatButton.Group
      trigger="click"
      type="primary"
      style={{ right: 24 }}
      icon={<CustomerServiceOutlined />}
    >
      <FloatButton />
      <FloatButton icon={<CommentOutlined />} />
    </FloatButton.Group>
    <FloatButton.Group
      trigger="hover"
      type="primary"
      style={{ right: 94 }}
      icon={<CustomerServiceOutlined />}
    >
      <FloatButton />
      <FloatButton icon={<CommentOutlined />} />
    </FloatButton.Group>
  </>
);

export default App;
```

## badge-debug demo
>/demo/badge-debug.tsx


调试使用。



debug use.
```tsx
import React, { useState } from 'react';
import { ConfigProvider, FloatButton, Slider } from 'antd';
import type { ConfigProviderProps, GetProp } from 'antd';

type AliasToken = GetProp<ConfigProviderProps, 'theme'>['token'];

const App: React.FC = () => {
  const [radius, setRadius] = useState<number>(0);

  const token: Partial<AliasToken> = {
    borderRadius: radius,
  };

  return (
    <>
      <Slider min={0} max={20} style={{ margin: 16 }} onChange={setRadius} />
      <ConfigProvider theme={{ token }}>
        <FloatButton shape="square" badge={{ dot: true }} />
      </ConfigProvider>
    </>
  );
};

export default App;
```

## badge demo
>/demo/badge.tsx


右上角附带圆形徽标数字的悬浮按钮。



FloatButton with Badge.
```tsx
import { QuestionCircleOutlined } from '@ant-design/icons';
import React from 'react';
import { FloatButton } from 'antd';

const App: React.FC = () => (
  <>
    <FloatButton shape="circle" badge={{ dot: true }} style={{ right: 24 + 70 + 70 }} />
    <FloatButton.Group shape="circle" style={{ right: 24 + 70 }}>
      <FloatButton
        href="https://ant.design/index-cn"
        tooltip={<div>custom badge color</div>}
        badge={{ count: 5, color: 'blue' }}
      />
      <FloatButton badge={{ count: 5 }} />
    </FloatButton.Group>
    <FloatButton.Group shape="circle">
      <FloatButton badge={{ count: 12 }} icon={<QuestionCircleOutlined />} />
      <FloatButton badge={{ count: 123, overflowCount: 999 }} />
      <FloatButton.BackTop visibilityHeight={0} />
    </FloatButton.Group>
  </>
);

export default App;
```

## basic demo
>/demo/basic.tsx


最简单的用法。



The most basic usage.
```tsx
import React from 'react';
import { FloatButton } from 'antd';

const App: React.FC = () => <FloatButton onClick={() => console.log('onClick')} />;

export default App;
```

## back-top demo
>/demo/back-top.tsx


返回页面顶部的操作按钮。



`BackTop` makes it easy to go back to the top of the page.
```tsx
import React from 'react';
import { FloatButton } from 'antd';

const App: React.FC = () => (
  <div style={{ height: '300vh', padding: 10 }}>
    <div>Scroll to bottom</div>
    <div>Scroll to bottom</div>
    <div>Scroll to bottom</div>
    <div>Scroll to bottom</div>
    <div>Scroll to bottom</div>
    <div>Scroll to bottom</div>
    <div>Scroll to bottom</div>
    <FloatButton.BackTop />
  </div>
);

export default App;
```
