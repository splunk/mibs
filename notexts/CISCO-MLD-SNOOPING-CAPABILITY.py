#
# PySNMP MIB module CISCO-MLD-SNOOPING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MLD-SNOOPING-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMldSnoopingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 586))
ciscoMldSnoopingCapability.setRevisions(('2010-03-02 00:00',))
if mibBuilder.loadTexts: ciscoMldSnoopingCapability.setLastUpdated('201003020000Z')
if mibBuilder.loadTexts: ciscoMldSnoopingCapability.setOrganization('Cisco Systems, Inc.')
ciscoMldSnoopingCapabilityV04R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 586, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMldSnoopingCapabilityV04R01 = ciscoMldSnoopingCapabilityV04R01.setProductRelease('Cisco IOS-XR')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMldSnoopingCapabilityV04R01 = ciscoMldSnoopingCapabilityV04R01.setStatus('current')
mibBuilder.exportSymbols("CISCO-MLD-SNOOPING-CAPABILITY", PYSNMP_MODULE_ID=ciscoMldSnoopingCapability, ciscoMldSnoopingCapability=ciscoMldSnoopingCapability, ciscoMldSnoopingCapabilityV04R01=ciscoMldSnoopingCapabilityV04R01)
