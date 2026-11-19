#
# PySNMP MIB module CISCO-PSM-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-PSM-MIB-CAPABILITY
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
ciscoPsmMibCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoPsmMibCapability.setRevisions(('2003-08-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPsmMibCapability.setRevisionsDescriptions(('The capabilities description of \n                                 Cisco Port Security MIB for\n                                 MDS 1.2(1).',))
if mibBuilder.loadTexts: ciscoPsmMibCapability.setLastUpdated('200308050000Z')
if mibBuilder.loadTexts: ciscoPsmMibCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPsmMibCapability.setContactInfo('       Cisco Systems\n                                        Customer Service\n\n                                Postal: 170 West Tasman Drive\n                                        San Jose, CA  95134\n                                        USA\n\n                                Tel: +1 800 553-NETS\n\n                                E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoPsmMibCapability.setDescription('Agent capabilities for \n                                 CISCO-PSM-MIB')
ciscoPsmMibCapabilityMDS12R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPsmMibCapabilityMDS12R0 = ciscoPsmMibCapabilityMDS12R0.setProductRelease('Cisco MDS 1.2(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPsmMibCapabilityMDS12R0 = ciscoPsmMibCapabilityMDS12R0.setStatus('current')
if mibBuilder.loadTexts: ciscoPsmMibCapabilityMDS12R0.setDescription('Cisco Port Security MIB capabilities')
mibBuilder.exportSymbols("CISCO-PSM-MIB-CAPABILITY", PYSNMP_MODULE_ID=ciscoPsmMibCapability, ciscoPsmMibCapability=ciscoPsmMibCapability, ciscoPsmMibCapabilityMDS12R0=ciscoPsmMibCapabilityMDS12R0)
