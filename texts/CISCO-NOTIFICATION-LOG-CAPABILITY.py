#
# PySNMP MIB module CISCO-NOTIFICATION-LOG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-NOTIFICATION-LOG-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoNotificationLogCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 463))
ciscoNotificationLogCapability.setRevisions(('2008-12-18 00:00', '2007-01-22 00:00', '2005-11-29 00:00', '2005-11-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoNotificationLogCapability.setRevisionsDescriptions(('Added agent Capability for NX-OS 4.1(3)', 'Added agent Capability for IOS XR 3.4 on CRS-1', 'Added CAPABILITY macro for 12.2S.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoNotificationLogCapability.setLastUpdated('200812180000Z')
if mibBuilder.loadTexts: ciscoNotificationLogCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoNotificationLogCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoNotificationLogCapability.setDescription('Agent capabilities for NOTIFICATION-LOG-MIB')
cNotificationLogCapabilityV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 463, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cNotificationLogCapabilityV12R04 = cNotificationLogCapabilityV12R04.setProductRelease('Cisco IOS 12.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cNotificationLogCapabilityV12R04 = cNotificationLogCapabilityV12R04.setStatus('current')
if mibBuilder.loadTexts: cNotificationLogCapabilityV12R04.setDescription('NOTIFICATION-LOG-MIB capabilities')
cNotificationLogCapabilityV12R2S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 463, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cNotificationLogCapabilityV12R2S = cNotificationLogCapabilityV12R2S.setProductRelease('Cisco IOS 12.2S and 12.2S based releases')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cNotificationLogCapabilityV12R2S = cNotificationLogCapabilityV12R2S.setStatus('current')
if mibBuilder.loadTexts: cNotificationLogCapabilityV12R2S.setDescription('NOTIFICATION-LOG-MIB capabilities')
cNotificationLogCapIOSXRV3R4CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 463, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cNotificationLogCapIOSXRV3R4CRS1 = cNotificationLogCapIOSXRV3R4CRS1.setProductRelease('Cisco IOS XR 3.4 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cNotificationLogCapIOSXRV3R4CRS1 = cNotificationLogCapIOSXRV3R4CRS1.setStatus('current')
if mibBuilder.loadTexts: cNotificationLogCapIOSXRV3R4CRS1.setDescription('NOTIFICATION-LOG-MIB capabilities')
cNotificationLogCapNXOSV04R0103 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 463, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cNotificationLogCapNXOSV04R0103 = cNotificationLogCapNXOSV04R0103.setProductRelease('Cisco NX-OS 4.1(3) on MDS9000 and Nexus7000 Storage Switches')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cNotificationLogCapNXOSV04R0103 = cNotificationLogCapNXOSV04R0103.setStatus('current')
if mibBuilder.loadTexts: cNotificationLogCapNXOSV04R0103.setDescription('NOTIFICATION-LOG-MIB capabilities')
mibBuilder.exportSymbols("CISCO-NOTIFICATION-LOG-CAPABILITY", PYSNMP_MODULE_ID=ciscoNotificationLogCapability, cNotificationLogCapIOSXRV3R4CRS1=cNotificationLogCapIOSXRV3R4CRS1, cNotificationLogCapNXOSV04R0103=cNotificationLogCapNXOSV04R0103, cNotificationLogCapabilityV12R2S=cNotificationLogCapabilityV12R2S, cNotificationLogCapabilityV12R04=cNotificationLogCapabilityV12R04, ciscoNotificationLogCapability=ciscoNotificationLogCapability)
