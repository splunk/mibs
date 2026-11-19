#
# PySNMP MIB module VELOCLOUD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VELOCLOUD-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:40:58 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, IpAddress, NotificationType, ObjectIdentity, TimeTicks, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, enterprises, Integer32, Gauge32, Counter32, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "NotificationType", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "enterprises", "Integer32", "Gauge32", "Counter32", "Bits", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
velocloud = ModuleIdentity((1, 3, 6, 1, 4, 1, 45346))
velocloud.setRevisions(('2021-05-11 00:00', '2019-08-02 00:00', '2017-01-18 00:00', '2017-01-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: velocloud.setRevisionsDescriptions(('Update of VMware nomenclature', 'Implementation of VMware SD-WAN Edge MIB Objects', 'Implementation of VCO MIB Objects', 'Inital definition of VMware SD-WAN MIB Objects',))
if mibBuilder.loadTexts: velocloud.setLastUpdated('202105110000Z')
if mibBuilder.loadTexts: velocloud.setOrganization('VMware Corporation')
if mibBuilder.loadTexts: velocloud.setContactInfo('postal:    VMware Corporation \n                                    World Headquarters\n                                    3401 Hillview Avenue\n                                    Palo Alto, CA 943043\n                                    USA\n                        \n                         web:       sase.vmware.com')
if mibBuilder.loadTexts: velocloud.setDescription('Top-level infrastructure of the VMware SD-WAN enterprise MIB tree')
modules = MibIdentifier((1, 3, 6, 1, 4, 1, 45346, 1))
mibBuilder.exportSymbols("VELOCLOUD-MIB", modules=modules, velocloud=velocloud, PYSNMP_MODULE_ID=velocloud)
