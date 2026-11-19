#
# PySNMP MIB module CISCO-NOTIFICATION-LOG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-NOTIFICATION-LOG-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoNotificationLogCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 463))
ciscoNotificationLogCapability.setRevisions(('2008-12-18 00:00', '2007-01-22 00:00', '2005-11-29 00:00', '2005-11-18 00:00',))
if mibBuilder.loadTexts: ciscoNotificationLogCapability.setLastUpdated('200812180000Z')
if mibBuilder.loadTexts: ciscoNotificationLogCapability.setOrganization('Cisco Systems, Inc.')
cNotificationLogCapabilityV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 463, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cNotificationLogCapabilityV12R04 = cNotificationLogCapabilityV12R04.setProductRelease('Cisco IOS 12.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cNotificationLogCapabilityV12R04 = cNotificationLogCapabilityV12R04.setStatus('current')
cNotificationLogCapabilityV12R2S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 463, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cNotificationLogCapabilityV12R2S = cNotificationLogCapabilityV12R2S.setProductRelease('Cisco IOS 12.2S and 12.2S based releases')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cNotificationLogCapabilityV12R2S = cNotificationLogCapabilityV12R2S.setStatus('current')
cNotificationLogCapIOSXRV3R4CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 463, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cNotificationLogCapIOSXRV3R4CRS1 = cNotificationLogCapIOSXRV3R4CRS1.setProductRelease('Cisco IOS XR 3.4 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cNotificationLogCapIOSXRV3R4CRS1 = cNotificationLogCapIOSXRV3R4CRS1.setStatus('current')
cNotificationLogCapNXOSV04R0103 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 463, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cNotificationLogCapNXOSV04R0103 = cNotificationLogCapNXOSV04R0103.setProductRelease('Cisco NX-OS 4.1(3) on MDS9000 and Nexus7000 Storage Switches')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cNotificationLogCapNXOSV04R0103 = cNotificationLogCapNXOSV04R0103.setStatus('current')
mibBuilder.exportSymbols("CISCO-NOTIFICATION-LOG-CAPABILITY", ciscoNotificationLogCapability=ciscoNotificationLogCapability, PYSNMP_MODULE_ID=ciscoNotificationLogCapability, cNotificationLogCapabilityV12R04=cNotificationLogCapabilityV12R04, cNotificationLogCapIOSXRV3R4CRS1=cNotificationLogCapIOSXRV3R4CRS1, cNotificationLogCapabilityV12R2S=cNotificationLogCapabilityV12R2S, cNotificationLogCapNXOSV04R0103=cNotificationLogCapNXOSV04R0103)
