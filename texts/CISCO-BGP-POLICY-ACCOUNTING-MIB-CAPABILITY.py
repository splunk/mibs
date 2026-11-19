#
# PySNMP MIB module CISCO-BGP-POLICY-ACCOUNTING-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-BGP-POLICY-ACCOUNTING-MIB-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cbpAcctCapabilitity = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 468))
cbpAcctCapabilitity.setRevisions(('2005-12-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cbpAcctCapabilitity.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: cbpAcctCapabilitity.setLastUpdated('200512300000Z')
if mibBuilder.loadTexts: cbpAcctCapabilitity.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cbpAcctCapabilitity.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com\n                        cs-snmp@cisco.com')
if mibBuilder.loadTexts: cbpAcctCapabilitity.setDescription('The capabilities description of\n                 CISCO-BGP-POLICY-ACCOUNTING-MIB.')
cbgppaCapabilityIOSXRV3R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 468, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbgppaCapabilityIOSXRV3R0CRS1 = cbgppaCapabilityIOSXRV3R0CRS1.setProductRelease('Cisco IOS XR 3.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbgppaCapabilityIOSXRV3R0CRS1 = cbgppaCapabilityIOSXRV3R0CRS1.setStatus('current')
if mibBuilder.loadTexts: cbgppaCapabilityIOSXRV3R0CRS1.setDescription('CISCO-BGP-POLICY-ACCOUNTING-MIB \n                        capabilities for IOS XR release 3.0')
mibBuilder.exportSymbols("CISCO-BGP-POLICY-ACCOUNTING-MIB-CAPABILITY", PYSNMP_MODULE_ID=cbpAcctCapabilitity, cbgppaCapabilityIOSXRV3R0CRS1=cbgppaCapabilityIOSXRV3R0CRS1, cbpAcctCapabilitity=cbpAcctCapabilitity)
