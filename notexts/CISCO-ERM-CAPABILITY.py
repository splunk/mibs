#
# PySNMP MIB module CISCO-ERM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ERM-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoErmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 492))
ciscoErmCapability.setRevisions(('2006-03-09 00:00',))
if mibBuilder.loadTexts: ciscoErmCapability.setLastUpdated('200603090000Z')
if mibBuilder.loadTexts: ciscoErmCapability.setOrganization('Cisco Systems, Inc.')
ciscoErmCapabilityV12R02SR = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 492, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErmCapabilityV12R02SR = ciscoErmCapabilityV12R02SR.setProductRelease('Cisco IOS 12.2SR')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErmCapabilityV12R02SR = ciscoErmCapabilityV12R02SR.setStatus('current')
mibBuilder.exportSymbols("CISCO-ERM-CAPABILITY", ciscoErmCapability=ciscoErmCapability, ciscoErmCapabilityV12R02SR=ciscoErmCapabilityV12R02SR, PYSNMP_MODULE_ID=ciscoErmCapability)
